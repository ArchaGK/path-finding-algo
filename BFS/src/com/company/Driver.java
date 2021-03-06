package com.company;

/**
 * Our main driver class which instantiates some example nodes
 * and then performs the breadth first search upon these newly created
 * nodes.
 */
public class Driver {

    public static void main(String args[]){
        Node station1 = new Node("Westminster", null, null);
        Node station2 = new Node("Waterloo", station1, null);
        Node station3 = new Node("Trafalgar Square", station1, station2);
        Node station4 = new Node("Canary Wharf", station2, station3);
        Node station5 = new Node("London Bridge", station4, station3);
        Node station6 = new Node("Tottenham Court Road", station5, station4);

        BreadthFirstSearch bfs = new BreadthFirstSearch(station6, station1);

        if(bfs.compute())
            System.out.print("Path Found!");
    }
}

/*

    List<Map<String,List<String>>> list = new ArrayList<Map<String,List<String>>>();//This is the final list you need
    Map<String, List<String>> map1 = new HashMap<String, List<String>>();//This is one instance of the  map you want to store in the above list.
    List<String> arraylist1 = new ArrayList<String>();
arraylist1.add("Text1");//And so on..
        map1.put("key1",arraylist1);
//And so on...
        list.add(map1);//In this way you can add.
*/
