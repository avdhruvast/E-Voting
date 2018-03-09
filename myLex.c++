//#include <stdio.h>
#include <iostream>
using namespace std;
#include <stdlib.h>
#include "y.tab.h"
extern yylType yylval;
int  main() // myLex.c
{
     int s;

     while((s=yylex()))
     switch(s) {
      case '\n': cout << "\n";
                 break;
      case '(' : cout << "<(> ";
                 break;
      case ')' : cout << "<)> ";
                 break;
      case '{' : cout << "<{> ";
                 break;
      case '}' : cout << "<}> ";
                 break;
      case ';' : cout << "<;> ";
                 break;
      case ',' : cout << "<,> ";
                 break;
      case '=' : cout << "<=> ";
                 break;
      case '<' : cout << "<<> ";
                 break;
      case BIN_OP : cout << "<BIN_OP," << (char) yylval.integer << "> ";
                    break;
      case IF  : cout << "<if> ";
                 break;
      case ELSE : cout << "<else> ";
                  break;
      case WHILE : cout << "<while> ";
                   break;
      case FOR : cout << "<for> ";
                 break;
      case INT : cout << "<int> ";
                 break;
      case ID  : cout << "<ID," << yylval.string << "> ";
                 free (yylval.string);
                 break;
      case NUM : cout << "<NUM," << yylval.integer << "> ";
                 break;
      case STRNG : cout << "<STRNG," << yylval.string << "> ";
                 free (yylval.string) ;
                 break;
      default:  ;
     }
     return 0;
}
