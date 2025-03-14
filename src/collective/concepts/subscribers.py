from OFS.ObjectManager import BeforeDeleteException
from plone import api


def on_add_book(book, event):
    current_user_fullname = api.user.get_current().getProperty("fullname")
    sender = api.user.get_current().getProperty("email")
    recipients = ["sebastien.verbois@gmail.com"]
    subject = "Nouveau livre ajouté"
    body = f"Le livre {book.title} avec ISBN-{book.isbn} été ajouté dans le site par {current_user_fullname}."
    api.portal.send_email(sender=sender, recipient=recipients, subject=subject, body=body)


def on_add_and_modify_book(book, event):
    if len(book.title) > 50:
        api.portal.show_message(message="Le titre du livre est un peu long :-)", type="warning")
    if len(book.title) <= 50 and len(book.authors) > 0 and api.content.get_state(obj=book) != "published":
        with api.env.adopt_roles(roles=["Reviewer"]):
            api.content.transition(obj=book, transition="publish")
            api.portal.show_message(message="Le livre a été publié.", type="info")


def on_after_transition_book(book, event):
    if event.action == "publish":
        with api.env.adopt_roles(roles=["Manager"]):
            portal = api.portal.get()
            book_folder = portal["livres"]
            api.content.move(source=book, target=book_folder)


def on_before_delete_book(book, event):
    if book.publisher == "apress":
        raise BeforeDeleteException("Vous ne pouvez pas supprimer un livre de Apress.")


def on_after_delete_book(book, event):
    current_user_fullname = api.user.get_current().getProperty("fullname")
    sender = api.user.get_current().getProperty("email")
    recipients = ["sebastien.verbois@gmail.com"]
    subject = "Livre supprimé"
    body = f"Le livre {book.title} avec ISBN-{book.isbn} été supprimer dans le site par {current_user_fullname}."
    api.portal.send_email(sender=sender, recipient=recipients, subject=subject, body=body)
