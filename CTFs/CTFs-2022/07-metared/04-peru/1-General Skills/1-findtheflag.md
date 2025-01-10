Unzip this [archive](https://drive.google.com/file/d/15pFs7BTOuJ4jrHZOAHNXfPWunY0K9fGl/view?usp=sharing) and find the file named 'oliver_twist.txt'

## Solucion

- Solo desempaquetar
- El archivo viene a la vista o usar find .

```bash               
┌──(kali㉿kali)-[~/…/ctfs2022/metared-4-stage-peru/generalskills/findaflag]
└─$ unzip great_author.zip                 
Archive:  great_author.zip
   creating: great_author/
  inflating: great_author/14789.txt.utf-8  
  inflating: great_author/13771.txt.utf-8  
   creating: great_author/adequate_books/
  inflating: great_author/adequate_books/44578.txt.utf-8  
  inflating: great_author/adequate_books/46804-0.txt  
   creating: great_author/adequate_books/more_books/
   creating: great_author/adequate_books/more_books/.secret/
   creating: great_author/adequate_books/more_books/.secret/deeper_secrets/
   creating: great_author/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/
 extracting: great_author/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/Oliver_Twist.txt  
  inflating: great_author/adequate_books/more_books/1023.txt.utf-8  
   creating: great_author/satisfactory_books/
  inflating: great_author/satisfactory_books/16021.txt.utf-8  
   creating: great_author/satisfactory_books/more_books/
  inflating: great_author/satisfactory_books/more_books/37121.txt.utf-8  
  inflating: great_author/satisfactory_books/23765.txt.utf-8  
   creating: great_author/acceptable_books/
  inflating: great_author/acceptable_books/17879.txt.utf-8  
  inflating: great_author/acceptable_books/17880.txt.utf-8  
   creating: great_author/acceptable_books/more_books/
  inflating: great_author/acceptable_books/more_books/40723.txt.utf-8  
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/metared-4-stage-peru/generalskills/findaflag]
└─$ cat great_author/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/Oliver_Twist.txt  

fl@g{Ch@rRl3$_D1cK3N$}
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/metared-4-stage-peru/generalskills/findaflag]
└─$ 
```