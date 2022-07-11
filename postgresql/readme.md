Operacions :

- insert()
- insert_many()
- select()
- select_all()
- update()
- update_multiple_columns()
- delete()
- delete_all()

Per fer commit dels canvis: --> guardar-los
     table.commit()
     
 Per finalitzar la connexió amb la Base de Dades:
 
     - tancar la connexio sense fer commit dels canvis
     table.close()

     - fer commit dels canvis i després tancar la connexió
     table.close(True)
     - o també de manera més explicita: table.close("commit")
 
Hi ha varies maneres per inserir en podem destacar dues:
    - insert(**column_value) 
        aquest mètode pren arguments de paraula clau (nom = valor) el nom és la columna, valor és el valor que cal inserir:
          table.insert(
            city = 'fayoum',
           address = 'south of cairo'
         )
      
    - insert_many(columns, rows)
        columnes -han de ser de llista o tuple- columnes que s'han d'inserir files -han de ser valors de llista bidimensional o tuple bidimensional- que s'han d'inserir:
            table.insert_many(
              columns = ('city', 'address'),
               rows = [
                  ['matrooh', 'north'],
                ['luxor', 'south']
               ]
             )
    # CONTINUARÀ...
        
    
