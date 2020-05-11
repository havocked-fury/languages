#include <iostream>
#include <string>
#include <map>
#include <fstream>

int main(){
    std::ifstream inFile;
    inFile.open("input.txt");

    std::string word;
    std::map<std::string, int> mp;

    while(inFile >> word){
        if(mp.find(word) == mp.end()){
            mp[word]=1;    
        }
        else{
            mp[word]++;
        }
    }

    for(auto it:mp){
        std::cout<< it->first << ' ' << it->second << std::endl;
    }

    return 0;
}
