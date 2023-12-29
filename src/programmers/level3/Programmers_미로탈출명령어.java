package programmers.level3;

public class Programmers_미로탈출명령어 {

    // (x, y) -> (r, c)로 k이동만에 도착하는 경로 중
    // 사전순으로 제일 빠른 경로여야함 (dlru) 
    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        String answer = "";
        int width = Math.abs(y - c);
        int height = Math.abs(x - r);
        if ((k - width + height) % 2 != 0) return "impossible";

        int dNum = 0;
        int lNum = 0;
        int rlNum = 0;
        int rNum = 0;
        int uNum = 0;
        int dSpare = 0;
        int lSpare = 0;

        k = k - width - height;
        System.out.println(k);

        if (r > x) dNum += height;
        else uNum += height;
        if (c < y) lNum += width;
        else rNum += width;

        dSpare = Math.min(k / 2, n - Math.max(x, r));
        k -= dSpare * 2;

        lSpare = Math.min(k / 2, Math.min(c, y) - 1);
        k -= lSpare * 2;

        rlNum = k / 2;

        return new String("d").repeat(dNum + dSpare)
                + new String("l").repeat(lNum + lSpare)
                + new String("rl").repeat(rlNum)
                + new String("r").repeat(rNum + lSpare)
                + new String("u").repeat(uNum + dSpare);
    }
}
