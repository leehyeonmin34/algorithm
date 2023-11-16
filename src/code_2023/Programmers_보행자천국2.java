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
    enum Sign{
            VALID(0),
        INVALID(1),
        UNTURNABLE(2)
                    ;
        public final int value;
        private Sign(int value){
            this.value = value;
        }
    }

    int solution(int m, int n, int[][] cityMap) {
        int[][][] route = new int[m + 1][n + 1][2];
        M = m;
        N = n;

        // 제일먼저 위에서 아래로, 점점 오른쪽으로 경로수를 찾아나감
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                switch (cityMap[i][j]){
                    case 0:
                        int routeNumToNext = i == 0 && j == 0 ? 1 : routeNumTo(i, j, route);
                        route[i + 1][j][DOWN] = routeNumToNext;
                        route[i][j + 1][RIGHT] = routeNumToNext;
                        makeZeroIfNextPointIsInvalid(i, j, route, cityMap);
                        continue;
                    case 2:
                        route[i + 1][j][DOWN] = route[i][j][DOWN];
                        route[i][j + 1][RIGHT] = route[i][j][RIGHT];
                        makeZeroIfNextPointIsInvalid(i, j, route, cityMap);
                        continue;
                }
            }
        }
        System.out.println(Arrays.deepToString(route));
        return routeNumTo(m - 1, n - 1, route) % MOD;
    }


    int routeNumTo(int i, int j, int[][][] route){
        return route[i][j][RIGHT] + route[i][j][DOWN];
    }

    void makeZeroIfNextPointIsInvalid(int i, int j, int route[][][], int[][] map){
        makeZeroIfOne(i + 1, j, route, map);
        makeZeroIfOne(i, j + 1, route, map);
    }

    void makeZeroIfOne(int i, int j, int route[][][], int[][] map){
        if (i < M && j < N && map[i][j] == Sign.INVALID.value){
            route[i][j][RIGHT] = 0;
            route[i][j][DOWN] = 0;
        }
    }

}

