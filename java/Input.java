import java.util.*;

class Book {
	String author, title;

	Book() {
		author = "DEFAULT";
		title = "DEFAULT";
	}

	Book(String titleInput, String authorInput) {
		title = titleInput;
		author = authorInput;
	}

	String getAuthor(){
		return author;
	}

	String getTitle(){
		return title;
	}
}

public class Input {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String titleInput, authorInput;

		System.out.println("Enter Title: ");
		titleInput = sc.nextLine();

		System.out.println("Enter Author: ");
		authorInput = sc.nextLine();

		Book bookVar = new Book(titleInput, authorInput);

		System.out.println("Book \n Title: \t " + bookVar.getTitle() + "\n Author: \t " + bookVar.getAuthor());
	}
}