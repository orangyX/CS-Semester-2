import java.io.*;
import java.util.*;

public class aplusb {


	public static void main(String[] args) throws IOException 
    {
		BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter pw = new PrintWriter(System.out);

        StringTokenizer st = new StringTokenizer(r.readLine());

        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());

        pw.println(a + b);
		pw.close();
	}
}
