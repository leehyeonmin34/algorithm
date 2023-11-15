package code_2023;

// https://school.programmers.co.kr/learn/courses/30/lessons/1832?language=java

public class Programmers_보행자천국 {

    public static void main(String[] args) {
        Programmers_보행자천국 solution = new Programmers_보행자천국();
        System.out.println(solution.solution(3, 3, new int[][] {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}}));
    }

    //public class Solution {
    final int MOD = 20170805;
    final int RIGHT = 1;
    final int DOWN = 0;


    int solution(int m, int n, int[][] cityMap) {
        int answer = 0;
        int[][][] route = new int[m + 1][n + 1][2];

        // 기존 맵의 왼쪽과 위쪽에 갈 수 없는 지점을 생성함
        int[][] map = new int[m + 1][n + 1];
        for(int j = 1; j <= n; j++){
            for(int i = 1; i <= m; i++){
                map[i][j] = map[i - 1][j - 1];
            }
        }

        // 제일먼저 위에서 아래로, 점점 오른쪽으로 경로수를 찾아나감
        for(int j = 1; j < n; j++){
            for(int i = 1; i < m; i++){
                int routeToUp = routeNumTo(i - 1, j, map, route);
                int routeToLeft = routeNumTo(i, j -1, map, route);
                route[i][j][RIGHT] = routeToLeft == 0 ? 0 : routeToLeft + 1;
                route[i][j][DOWN] = routeToUp == 0 ? 0 : routeToUp + 1;
            }
        }

        return map[m][n] % MOD;
    }

    int routeNumTo(int i, int j, int[][] map, int[][][] route){
        return routeNumToWithDirection(RIGHT, i, j, map, route) + routeNumToWithDirection(DOWN, i, j, map, route);
    }

    int routeNumToWithDirection(int direction, int i, int j, int[][] map, int[][][] route){
        // 지난 지점으로의 경로가 없다면 그 경로를 통해 그 다음 지점(i, j)도 못감
//        if (direction == RIGHT && noRouteTo(i, j - 1, route)) return 0;
//        if (direction == DOWN && noRouteTo(i - 1, j, route)) return 0;

        // 지난 지점으로의 경로가 있다면, 통행불가를 제외하고는 이동 가능
        if(map[i][j] == 0 || map[i][j] == 2) return route[i][j][RIGHT] + route[i][j][DOWN]; // 이동 가능
        if(map[i][j] == 1) return 0; // 자동차 이동 불가능
        else{ // 회전 불가
            int answer = 0;
            if (direction == RIGHT) {
                return map[i][j - 1] == 1 ? route[i][j - 1][RIGHT] : 0;
            }
            else return route[i - 1][j][DOWN];
        }
    }

    boolean noRouteTo(int i, int j, int[][][] route){
        return route[i][j][RIGHT] + route[i][j][DOWN] == 0 ? true : false;
    }
}

