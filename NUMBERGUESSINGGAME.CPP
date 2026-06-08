
#include<iostream> // input 
#include<ctime>  // time
#include<cstdlib>  // for randomized the number
using namespace std;
int main() {

    srand(time(0));
    
    int x;
    cout<<"ENTER THE NUMBER : "<<endl;
    cin>>x;

    int randomnumber = rand()%10 + 1;
    cout<< randomnumber <<endl;

    if (x >= 1 && x <= 10 && x == randomnumber){
    cout<<"wow! you win "<<endl;}
    
    else if(x<1 or x>10 ){
    cout<<"NOT POSSIBLE BRO! NUMBER WILL BE ONLY FORM 1 TO 10 "<<endl;}

    else{
    cout<<"shhh! you  lose "<<endl;}
}
