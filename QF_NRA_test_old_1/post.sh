#！/bin/bash

function post_process() {
    for file in $@/*;do 
        sed -i -r 's/_[0-9]+\//\//g' $file
        sed -i -r 's/temp\///g' $file
        sed -i -r 's/_split//g' $file
        sed -i -r 's/_hard//g' $file
    done
}

post_process $1