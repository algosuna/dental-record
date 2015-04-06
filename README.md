Because I like lists - Andrea

## Latest

TODO: 12-mar-2015
-----------------

- client detail view
    - ~~latest procedures~~
    - past procedures
    - ~~new odontogram~~
    - ~~edit latest odontogram (nope)~~
    ### Update 13-mar-2015
    - ~~add notes field to Procedimientos~~
    - ~~separate diagnostics from procerures~~

TODO: 13-mar-2015
-----------------

- ~~connection to cotizacion~~
    - ~~model rethinking~~
    - flow of the administrative section
        - ~~start - view of pending service orders~~
        - ~~then - generate quote~~
        - ~~then - update item status~~
        - ~~then - go to payment~~
        - then - services with total payment go to approved orders and you print receipt for client
    - prefix on cotizacion id (models.py) (maybe)

TODO: 23-mar-2015
-----------------

- connection to payment process
- price - make sure it can't be empty. ask for user to add prices after registering group.
    - ~~add precio field to Tratamiento~~ (creo que fue ray)
    - default to a standard
    - user flow - from registering group to add prices
    - ...


## Old and Done

## ~~TODO: 10-mar-2015~~

- ~~odontograma detail view~~
    - ~~with a summary of the registered procedimientos~~
    - ~~details of the client~~
    - ~~relate procedimientos to odontograma id~~
    - ~~relate odontograma id to client id~~
    - ~~button goes to client detail view~~
