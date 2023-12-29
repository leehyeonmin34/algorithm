package programmers.level3;

// https://school.programmers.co.kr/learn/courses/30/lessons/1832?language=java

public class Programmers_보행자천국 {

    public static void main(String[] args) {
        Programmers_보행자천국 solution = new Programmers_보행자천국();
        System.out.println(solution.solution(3, 3, new int[][] {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}}));
        System.out.println(solution.solution(3, 6, new int[][]{{0, 2, 0, 0, 0, 2},{0, 0, 2, 0, 1, 0},{1, 0, 0, 2, 2, 0}}));
    }

    final int MOD = 20170805;
    final int DOWN = 0;
    final int RIGHT = 1;
    final int VALID_SIGN = 0;
    final int UNTURNABLE_SIGN = 2;

    private int solution(int m, int n, int[][] cityMap) {
        int[][][] route = new int[m + 1][n + 1][2];

        // 제일 윗줄부터 왼쪽에서 오른쪽으로 경로수를 찾아나감
        // route[i][j][RIGHT]는 RIGHT 방향으로 이동해서 i, j에 도착하는 경로수를 의미
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                switch (cityMap[i][j]){
                    case VALID_SIGN:
                        int routeNumToNext = i == 0 && j == 0 ? 1 : routeNumTo(i, j, route);
                        // (i,j)의 아래와 오른쪽의 경로수를 지정해줌.
                        route[i + 1][j][DOWN] = routeNumToNext % MOD; // 여기서 % MOD 처리 안해서 틀림. 아무래도 int 값 범위의 문제인듯
                        route[i][j + 1][RIGHT] = routeNumToNext % MOD;
                        continue;
                    case UNTURNABLE_SIGN:
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

