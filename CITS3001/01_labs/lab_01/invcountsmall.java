import java.io.*;
import java.util.*;

public class invcountsmall 
{
    static long ans = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter pw = new PrintWriter(System.out);

		StringTokenizer st = new StringTokenizer(r.readLine());
		int N = Integer.parseInt(st.nextToken());

        long[] arr = new long[N];

        st = new StringTokenizer(r.readLine());
        ans = 0;

        for(int i=0; i<N; i++)
        {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        mergeSort(arr);

		pw.println(ans);
		pw.close();
	}

    public static long[] mergeSort(long[] arr)
    {
        if(arr.length <= 1) return arr;

        int mid = (arr.length)/2;

        long[] left = Arrays.copyOfRange(arr, 0, mid);
        long[] right = Arrays.copyOfRange(arr, mid, arr.length);

        return merge(mergeSort(left), mergeSort(right));
    }

    public static long[] merge(long[] left, long[] right)
    {
        long[] result = new long[left.length + right.length];

        int l=0, r=0, index=0;

        while(l <left.length && r<right.length)
        {
            if(left[l] <= right[r])
            {
                result[index] = left[l];
                l++;
            }
            else
            {
                result[index] = right[r];
                r++;
                ans += left.length - l;
                
            }
            index++;
        }

        if(l < left.length)
        {
            while(index < result.length && l<left.length)
            {
                result[index] = left[l];
                index++;
                l++;
            }
        }
        if(r < right.length)
        {
            while(index < result.length && r<right.length)
            {
                result[index] = right[r];
                index++;
                r++;
            }
        }

        return result;
    }
}
