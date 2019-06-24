#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

// splitの定義
int split(int n, int w, char **dar, char *src, int del);

// 出力関数
int
show(int nf, char *far[])
{
    int i;
    for(i=0;i<nf;i++) {
        printf("%3d: %3d |%s|\n", i, (int)strlen(far[i]), far[i]);
    }
}


main(){
#define NF (10)
    char **chunk;
    int i;
    int j;
    int m;
    int ik;

#if 0
    srand(time(NULL));
#endif

    chunk = (char**)malloc(sizeof(char*)*NF);
    if(!chunk) {
        exit(3);
    }

    for(i=0;i<NF;i++) {
        chunk[i] = (char*)malloc(sizeof(char)*BUFSIZ);
        if(! chunk[i]) {
            exit(5);
        }
        m = rand()%36+3;
        for(j=0;j<m;j++) {
            chunk[i][j] = 'A'+(rand()%26);
        }
        chunk[i][j] = '\0';
    }

    /*
    show(NF, chunk);

    ik = split(NF, BUFSIZ, chunk, "ABC DEF GHI", ' ');
    printf("ik %d\n", ik);
    show(ik, chunk);
    ik = split(NF, BUFSIZ, chunk, "JKL MNO ", ' ');
    printf("ik %d\n", ik);
    show(ik, chunk);
    */

}

int 
split(int n, int w, char **dar, char *src, int del)
{
    int cnt =0;
    for(int i =0; i<n; i++){
        if (*src == '\0') break;
        while(*src == del){
            src++;
        }
        for(int j = 0; j<w; j++){
            if(*src && *src !=del){
                dar[i][j] =*src;
                src++;
            }
            else{
                if (j != 0) cnt++;
                dar[i][j] = '\0';
                break;
            }
        }
        if (*src == '\0') break;

    }
    return cnt;
}
