package com.company;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.HashMap;


/**
 * basic breadth first search in java
 */
public class BreadthFirstSearch {

    Node startNode;
    Node goalNode;

    public BreadthFirstSearch(Node start, Node goalNode){
        this.startNode = start;
        this.goalNode = goalNode;
    }

    public boolean compute(){

        if(this.startNode.equals(goalNode)){
            System.out.println("Goal Node Found!");
            System.out.println(startNode);
        }

        Queue<Node> queue = new LinkedList<>();
        ArrayList<Node> explored = new ArrayList<>();
//        ArrayList<String> forhash = new ArrayList<>();
//        HashMap<String, ArrayList<String>> hmap = new HashMap<String, ArrayList<String>>();





        queue.add(this.startNode);
        explored.add(startNode);
        int i =0;

        while(!queue.isEmpty()){
            Node current = queue.remove();
            if(current.equals(this.goalNode)) {
                System.out.println(explored);

                return true;
            }
            else{
                if(current.getChildren().isEmpty())
                    return false;
                else
                    queue.addAll(current.getChildren());
//                    System.out.println("printing hashmap "+hmap);
//                    ArrayList<String> array = new ArrayList<String>();
//
//
//                    if (current.rightChild !=null || current.leftChild !=null) {
//                        array.add(current.leftChild.stationName);
//                        array.add(current.rightChild.stationName);
//
//                        hmap.put(current.stationName, array);
//                   }

            }
            explored.add(current);
        }

        return false;

    }

}