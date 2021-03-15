/* Fucks Given Generator in C
 * (c) 2018 - Daniel Menelkir <menelkir@itroll.org>
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void printRandoms(int lo, int hi,
                             int count)
{
    int i;
    for (i = 0; i < count; i++) {
        int num = (rand() %
           (hi - lo + 1)) + lo;
        printf("%d! %d FUCKS GIVEN! HAHAHAHA!\n ", num);
    }
}

int main()
{
    int lo = 0, hi = 7, count = 1;
    srand(time(0));
    printRandoms(lo, hi, count);
    return 0;
}
