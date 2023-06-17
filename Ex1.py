import xml.etree.ElementTree as ET

# Открываем XML файл
tree = ET.parse('library.xml')
root = tree.getroot()

def add_book():
  # Получаем данные о новой книге от пользователя
  title = input("Enter book title: ")
  author = input("Enter book author: ")
  year = input("Enter book year: ")
  # Создаем новый элемент book
  new_book = ET.Element("book")
  # Создаем элементы title, author и year и заполняем их значениями
  title_element = ET.SubElement(new_book, "title")
  title_element.text = title
  author_element = ET.SubElement(new_book, "author")
  author_element.text = author
  year_element = ET.SubElement(new_book, "year")
  year_element.text = year
  # Добавляем новый элемент book в корневой элемент library
  root.append(new_book)
  # Сохраняем изменения в файл
  tree.write('library.xml')

def search_books_by_author(author):
  # Ищем все книги с заданным автором
  books = root.findall(".//book[author='"+author+"']")
  # Выводим найденные книги
  if len(books) > 0:
    print("Books by "+author+":")
    for book in books:
      print(book.find('title').text)
  else:
    print("No books found by "+author)

def search_books_by_year(year):
  # Ищем все книги с заданным годом издания
  books = root.findall(".//book[year='"+year+"']")
  # Выводим найденные книги
  if len(books) > 0:
    print("Books published in "+year+":")
    for book in books:
      print(book.find('title').text)
  else:
    print("No books found published in "+year)

def delete_book(title):
  # Ищем книгу с заданным названием
  book = root.find(".//book[title='"+title+"']")
  if book is not None:
    # Удаляем найденный элемент book
    root.remove(book)
    # Сохраняем изменения в файл
    tree.write('library.xml')
    print("Deleted book: "+title)
  else:
    print("Book not found: "+title)

# Пример использования функций
add_book()
search_books_by_author('George Orwell')
search_books_by_year('1951')
delete_book('The Lord of the Rings')