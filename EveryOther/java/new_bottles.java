class new_bottles{
	public static void main(String[] args) {

		//Test T and hello T  works, meaning it can call classes from any programs it just save in folder of it
		int beernum = 99;
		String bottles = " bottles ";
		while (beernum > 0) {
			if (beernum == 1)
				bottles = " bottle ";
			System.out.print(beernum + bottles + "of beer on the wall,");
			System.out.println(beernum + bottles + "of beer.");
			System.out.print("Take me down and pass it around,");
			beernum = beernum - 1;
			if (beernum == 0)
				System.out.println("no more bottles of beer on the wall.");
			else
				System.out.println(beernum + bottles + "of beer on the wall");
			System.out.println();
		}
		System.out.println("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.");
	}
}
