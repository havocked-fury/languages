class Day {
	enum DayName{ SATURDAY, SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY }
	DayName thisDay;
}

public class DayTest {
	public static void main(String[] args) {
		Day today = new Day();
		today.thisDay = Day.DayName.SATURDAY;
		System.out.println("Today : " + today.thisDay);
	}
}