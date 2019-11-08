<?php
for($i = 1; $i<=50; $i++){
    if ($i % 3 == 0){
        echo "buda <br>";
    }
    elseif ($i % 5 == 0){
        echo "pest <br>";
    }
    else{
        echo $i. "<br>";
    }
}
