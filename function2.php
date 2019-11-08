<!-- <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="">
    <form action="" method="GET">
        <textarea name="ta" id="" cols="30" rows="10"></textarea>
    <button type="submit" name ="submit">submit</button>
    </form>
    <?php
    if(isset($_GET['submit'])){
        $wordsfromtextarea = $_GET['ta'];
        echo str_word_count($wordsfromtextarea);
    }
    ?>
</body>
</html> -->


 <?php
//replace
//echo str_replace("denno","dennis", "my name is dennis"); 


//user defined functions
$x = 79;
function passmark($x){
    if($x >= "90"){
        echo "A";
    }elseif(("90" > $x) &&($x >= "80")){
        echo "B";
    }elseif(("80" > $x) &&($x >= "70")){
        echo "C";
    }elseif(("70" > $x) &&($x >= "60")){
        echo "D";
    }elseif(("60" > $x) &&($x >= "50")){
        echo "E";

    }else{
        echo "failed";
    }
}
$a = 30;
passmark($a);
?>