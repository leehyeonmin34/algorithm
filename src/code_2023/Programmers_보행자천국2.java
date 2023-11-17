package code_2023;

// https://school.programmers.co.kr/learn/courses/30/lessons/1832?language=java

import java.util.Arrays;

public class Programmers_보행자천국2 {

    public static void main(String[] args) {
        Programmers_보행자천국2 solution = new Programmers_보행자천국2();
        System.out.println(solution.solution(3, 3, new int[][] {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}}));
        System.out.println(solution.solution(3, 6, new int[][]{{0, 2, 0, 0, 0, 2},{0, 0, 2, 0, 1, 0},{1, 0, 0, 2, 2, 0}}));
    }

    final int MOD = 20170805;
    final int DOWN = 0;
    final int RIGHT = 1;
    int M = 0;
    int N = 0;
    final int VALID = 0;
    final int UNTURNABLE = 2;

    int solution(int m, int n, int[][] cityMap) {
        int[][][] route = new int[m + 1][n + 1][2];
        M = m;
        N = n;


        // 제일먼저 위에서 아래로, 점점 오른쪽으로 경로수를 찾아나감
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                switch (cityMap[i][j]){
                    case VALID:
                        int routeNumToNext = i == 0 && j == 0 ? 1 : routeNumTo(i, j, route);
                        route[i + 1][j][DOWN] = routeNumToNext % MOD;
                        route[i][j + 1][RIGHT] = routeNumToNext % MOD;
                        continue;
                    case UNTURNABLE:
                        route[i + 1][j][DOWN] = route[i][j][DOWN] % MOD;
                        route[i][j + 1][RIGHT] = route[i][j][RIGHT] % MOD;
                        continue;
                }
            }
        }
        return routeNumTo(m - 1, n - 1, route) % MOD;
    }

    int routeNumTo(int i, int j, int[][][] route){
        return route[i][j][RIGHT] + route[i][j][DOWN];
    }

}

