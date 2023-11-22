package programmers.level3;

import java.util.Arrays;

public class Programmers_광고삽입 {
    public static void main(String[] args) {
        Programmers_광고삽입 solution = new Programmers_광고삽입();

        // "01:30:59"
        System.out.println(solution.solution("02:03:55"	, "00:14:15", new String[] {"01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"}));

        // "01:00:00"
        System.out.println(solution.solution("99:59:59",	"25:00:00", new String[] {"69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"}));

        // "00:00:00"
        System.out.println(solution.solution("50:00:00", "50:00:00", new String[] {"15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"}));
    }

    private int front = 0;
    private int back = 0;
    private long currView = 0; // int 범위를 넘어갈 수 있음
    private long maxView = 0;
    private int maxViewPoint = 0;
    private int prevSec = 0;
    private int currSec = 0;

    public String solution(String playTime, String advTime, String[] logs) {
        // 이 알고리즘의 핵심 컨셉
        // 광고구간이 재생구간을 지나는 슬라이딩윈도우라고 생각했을 때,
        // '윈도우의 앞과 뒤의 시청인원이 변하게되는 윈도우 위치'의 앞 지점(광고 시작시간)들을 리스트로 만든다.
        // 각 지점으로 이동할 때 마다, 누적 뷰 수의 변화는 (현재시간 - 이전지점 시간) * (윈도우 끝 인원 - 윈도우 시작 인원)임을 이용해 view 수를 갱신하는 것
        //
        // 단점
        // 이 알고리즘은 초단위로 누적 view 수를 계산하지 않고, 한 개의 log마다 4번의 계산을 거친다.
        // 최대 playTime은 99*59*59 = 344,619이므로 344619/4 = 86,154.75 개 이상의 log가 있을 때 초단위 계산보다 계산을 많이하게 된다.
        // 영상이 100시간이 넘어갈 일보다 view log가 8.6만개보다 많을 일이 훨씬 많기 때문에 테스트케이스에서 초단위 갱신보다 더 느리다.
        // 초단위보다 뭔가 더 빠르게 할 수 있지 않을까 싶어서 이렇게 해봤지만 오히려 더 느릴 것 같다.

        final int START = 0; // 재생 시작 (광고 시작할 때 인원 +1)
        final int START_AFTER_AD = 1; // 광고 구간 끝에 재생 시작 (광고 끝나면 인원 +1)
        final int END = 2; // 재생 끝 (광고 시작할 때 인원 -1)
        final int END_AFTER_AD = 3; // 광고 구간 끝에 재생 끝 (광고 끝나면 인원 -1)

        final int play = getSecondFromTimeString(playTime);
        final int adv = getSecondFromTimeString(advTime);
        prevSec = -adv; // 슬라이딩윈도우의 오른쪽끝이 0초에 닿아있을때부터 시작함.

        // 윈도우의 앞과 뒤의 시청인원이 변하게되는 윈도우 위치의 앞 지점
        int[][] times = new int[logs.length * 4][2];
        for(int i = 0; i < logs.length; i++) {
            String[] startAndEndTime = logs[i].split("-");
            int start = getSecondFromTimeString(startAndEndTime[0]);
            int end = getSecondFromTimeString(startAndEndTime[1]);
            times[i * 4] = new int[] {start, START};
            times[i * 4 + 1] = new int[] {start - adv, START_AFTER_AD};
            times[i * 4 + 2] = new int[] {end, END};
            times[i * 4 + 3] = new int[] {end - adv, END_AFTER_AD};
        }
        Arrays.sort(times, (a, b) -> a[0] - b[0]);

        // 각 지점들을 돌며 view 수 갱신
        for(int[] time : times){
            currSec = time[0];
            int pointType = time[1];

            // 최댓값이 갱신될만한 때는 START와 END_AFTER_AD밖에 없음
            switch (pointType){
                case START:
                    reflectViewDiff();
                    compareAndRenewMaxView();
                    front += 1;
                    log();
                    continue;
                case START_AFTER_AD:
                    reflectViewDiff();
                    back += 1;
                    log();
                    continue;
                case END:
                    reflectViewDiff();
                    front -= 1;
                    log();
                    continue;
                case END_AFTER_AD:
                    reflectViewDiff();
                    compareAndRenewMaxView();
                    back -= 1;
                    log();
                    continue;
            }
        }

        return getTimeStringFromSec(maxViewPoint);

    }

    private void log(){
//        System.out.printf("%s : 현재 시작하면 %d view(max %d), 현재 인원 : %d / %d  %n"
//                , getTimeStringFromSec(currSec)
//                , currView
//                , maxView
//                , front
//                , back);
    }

    private void reflectViewDiff(){
        currView += (currSec - prevSec) * (back - front);
        prevSec = currSec;
    }

    private void compareAndRenewMaxView(){
        if (currView > maxView){
            maxView = currView;
            // 최대뷰를 가질 광고시작시간이 0초보다 전이라면, 그냥 0초에 시작한다고 간주해도 됨
            if (currSec < 0) maxViewPoint = 0;
            else maxViewPoint = currSec;
        }
    }

    private int getSecondFromTimeString(String timeString){
        String[] timeFrags = timeString.split(":");
        int hour = Integer.parseInt(timeFrags[0]);
        int min = Integer.parseInt(timeFrags[1]);
        int sec = Integer.parseInt(timeFrags[2]);
        return hour * 3600 + min * 60 + sec;
    }

    private String getTimeStringFromSec(int secInt){
        int hour = secInt / (3600);
        int min = (secInt / 60) % 60;
        int sec = secInt % 60;
        return String.format("%02d:%02d:%02d", hour, min, sec);
    }


}
