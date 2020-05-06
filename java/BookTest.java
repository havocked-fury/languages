class Book {
	String title, author;

	public Book(){
		title = "DEFAULT";
		author = "DEFAULT";
	}

	public Book(String title_, String author_) {
		title = title_;
		author = author_;
	}
}

public class BookTest {
	public static void main(String[] args) {
		Book testBook = new Book();
		Book testBook2 = new Book("Classical Mechanics", "J. R. Tylor");
		System.out.println("Book1, Title: " + testBook.title + " Author: " + testBook.author);
		System.out.println("Book2, Title: " + testBook2.title + " Author: " + testBook2.author);
	}
}