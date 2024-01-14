package programmers.level3;

import java.util.*;


// 프로그래머스의 user188245님의 풀이법
// 혼자 풀 땐 어려웠는데, 생각보다 풀이가 간단하다.
// 너무 복잡하게 생각하지 않아야겠다.
public class Programmers_표병합 {
    static final int cellsSize = 50;

    static final int boardSize = cellsSize*cellsSize;

    static final String empty = "EMPTY";

    static int[] rank;

    static int[] parent;

    static String[] board;

    static void init(){
        rank = new int[boardSize];
        parent = new int[boardSize];
        board = new String[boardSize];

        for(int i=1; i<boardSize; i++) {
            parent[i] = i;
        }

    }

    static int find(int r, int c) {
        return find(cellsSize*r+c);
    }

    // n의 으뜸을 찾는다.
    static int find(int n) {
        if(parent[n] == n) {
            return n;
        }
        return (parent[n] = find(parent[n]));
    }

    // a와 b를 병합한다. 이때, board의 내용은 a의 것으로 한다. a의 것이 없으면 b의 것으로 한다.
    static void union(int a, int b) {
        a = find(a);
        b = find(b);
        if(a==b) {
            return;
        }
        if(rank[a] < rank[b]) {
            parent[a] = b;
            // b가 마스터
            if(board[a] != null) {
                board[b] = board[a];
                board[a] = null;
            }
        }else {
            // a가 마스터
            parent[b] = a;
            if(rank[a] == rank[b]) {
                rank[a]++;
            }
            if(board[a] == null) {
                board[a] = board[b];
                board[b] = null;
            }
        }
    }


    // a와 으뜸이 같은 모든 셀을 해산시킨다. 그리고 모든 셀을 비워버린다. 셀에 있던 내용은 a가 가져간다.
    static void dismiss(int a) {
        for(int i=0; i<boardSize; i++) {
            find(i);
        }
        int x = find(a);
        String s = board[x];
        for(int i=0; i<boardSize; i++) {
            int y = find(i);
            if(x==y) {
                rank[i] = 0;
                parent[i] = i;
                board[i] = null;
            }
        }
        board[a] = s;
    }

    static void update(String value1, String value2) {
        for(int i=0; i<boardSize; i++) {
            if(board[i] != null && board[i].equals(value1)) {
                board[i] = value2;
            }
        }
    }

    static void update(int r, int c, String value) {
        int n = find(cellsSize*r+c);
        board[n] = value;
    }

    static void merge(int r1, int c1, int r2, int c2) {
        union(cellsSize*r1+c1, cellsSize*r2+c2);
    }

    static void unmerge(int r, int c) {
        dismiss(cellsSize*r + c);
    }

    static String print(int r, int c) {
        int n = find(cellsSize*r+c);
        if(board[n] == null) {
            return empty;
        }
        return board[n];
    }

    public void command(String comm, List<String> list) {
        String[] comms = comm.split(" ");
        String commName = comms[0];

        if(commName.equals("UPDATE")) {
            if(comms.length == 3) {
                String value1 = comms[1];
                String value2 = comms[2];
                update(value1, value2);
            }else {
                int r = Integer.parseInt(comms[1])-1;
                int c = Integer.parseInt(comms[2])-1;
                String value = comms[3];
                update(r,c,value);
            }
        }else if(commName.equals("MERGE")) {
            int r1 = Integer.parseInt(comms[1])-1;
            int c1 = Integer.parseInt(comms[2])-1;
            int r2 = Integer.parseInt(comms[3])-1;
            int c2 = Integer.parseInt(comms[4])-1;
            merge(r1,c1,r2,c2);
        }else if(commName.equals("UNMERGE")) {
            int r = Integer.parseInt(comms[1])-1;
            int c = Integer.parseInt(comms[2])-1;
            unmerge(r,c);
        }else if(commName.equals("PRINT")){
            int r = Integer.parseInt(comms[1])-1;
            int c = Integer.parseInt(comms[2])-1;
            list.add(print(r,c));
        }
    }

    public String[] solution(String[] commands) {
        List<String> list = new ArrayList<String>(1000);
        init();
        for(String command : commands) {
            command(command,list);
        }
        String[] answer = new String[list.size()];
        int i = 0;
        for(String s:list) {
            answer[i++] = s;
        }
        return answer;
    }
}