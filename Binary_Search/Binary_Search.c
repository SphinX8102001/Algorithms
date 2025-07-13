#include <stdio.h>

int binary_search(int arr[],int lengthOfArr,int target)
{   int low,high,mid;
    low = 0;
    high = lengthOfArr;
    while (high >= low)
    {
        mid = (low + high)/2;
        if (arr[mid] == target)
        {
            return mid;
        }
        else if (target > arr[mid])
        {
            low = mid + 1;
        }
        else if (target < arr[mid])
        {
            high = mid - 1;
        }
    }
    return -1;
}
int main()
{
    int lengthOfArr,target,output;
    printf("Enter length of Array: ");
    scanf("%d",&lengthOfArr);
    int Arr[lengthOfArr];
    printf("\nEnter %d elements of and array in increasing order: ",lengthOfArr);
    for (int i=0;i<lengthOfArr;i++)
    {
        scanf("%d",&Arr[i]);
    }
    printf("Enter Target: ");
    scanf("%d",&target);
    output = binary_search(Arr,lengthOfArr,target);
    if (output == -1)
    {
        printf("Target not found");
    }
    else
    {
        printf("Target at index: %d",output);
    }

}
