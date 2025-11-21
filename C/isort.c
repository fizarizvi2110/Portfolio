#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void sort_integer_array(int *begin, int *end, int ascending);

int main(){

        //Random generator reset
        srandom(time(NULL));

        //Getting input from user on array size
        int arrsize;
        printf("Please enter the size of the array as a positive integer: ");
        scanf("%d", &arrsize);

        //Allocating memory in the heap for the array
        int *original = (int *)malloc(arrsize * sizeof(int));

        //error message if malloc returns null for original array
        if (original == NULL){
                perror("malloc returned NULL");
                exit(1);
        }

        //Random number generator to fill array using modulus to ensure 0-99 values
        for(int i = 0; i < arrsize; i++){
                original[i] = random() % 100;
        }

        //Allocating memory in heap for sorted arrays
        int *ascendingarr = (int *)malloc(arrsize * sizeof(int));
        int *descendingarr = (int *)malloc(arrsize * sizeof(int));
        if (ascendingarr == NULL || descendingarr == NULL){
                perror("malloc returned NULL");
                exit(1);
        }

        //Copying array into second, ascending array
        for(int i = 0; i < arrsize; i++){
                ascendingarr[i] = original[i];
        }

        //Same for descending 
        for (int i = 0; i < arrsize; i++){
                descendingarr[i] = original[i];
        }

        //Calling sort methods on arrays
        sort_integer_array(ascendingarr, ascendingarr + arrsize, 1);
        sort_integer_array(descendingarr, descendingarr + arrsize, 0);

       //Printing results
        printf("original: ");
        for(int i = 0; i < arrsize; i++){
                printf("%d ", original[i]);
        }

        printf("\n");

        printf("ascending: ");
        for(int i = 0; i < arrsize; i++){
                printf("%d ", ascendingarr[i]);
        }

        printf("\n");

        printf("descending: ");
        for(int i = 0; i < arrsize; i++){
                printf("%d ", descendingarr[i]);
        }

        printf("\n");

        free(original);
        free(ascendingarr);
        free(descendingarr);

        return 0;

}

void sort_integer_array(int *begin, int *end, int ascending){
        int temp;
        int *i;
        for(i = begin; i < end - 1; i++){
                min = i;
                for(j = i + 1; j < end; j++){
                        if(ascending == 0){
                               if(*j  >  *min){
                                min = j;
                                }
                        }
                        else if (*j < *min){
                                min = j;
                        }
                }

                if(min != i){
                        temp = *(i);
                        *(i) = *(min);
                        *(min) = temp;
                }
        }
}

