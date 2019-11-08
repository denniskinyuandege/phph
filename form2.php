<?php
if(isset($_post["submit"])){
    $fname = $_post["firstname"];
    $lname = $_post["lastname"];
    $phone = $_post["phonenumber"];
    $Gender = $_post["Gender"];
    $date = $_post["date"];
    $Language = $_post["Language"];
    $Hobbies = $_post["Hobbies"];
    $email = $_post["e-mail"];
    $password = $_post["password"];
    $retypepassword = $_post["retypepassword"];  
    $address = $_post["address"];


    if(empty($fname)|| empty($lname) || empty($phone) || empty($Gender)|| empty($Language)||
     $Hobbies == '--' || empty($email)|| empty($password) || empty($retypepassword) ||{

        header("Location:form.php?fields=empty");
        exit();
     }elseif(!preg_match("/^[a-zA-Z]*$/",$fname) || !preg_match("/^[a-zA-Z]*$/",$lname) { 
        header("Location:form.php?fields=names");
        exit();
        // check if firstname and lastname is capital       
     }elseif(!ctype_upper($fname[0]) || !ctype_upper($fname[0])) {
        header("Location:form.php?fields=letter");
        exit();
      //phone number must be a number
     }elseif(!preg_match("/^[0-9]*$/",$fname)) {
      header("Location:form.php?fields=numbers");
      exit();
     }elseif (strpos($phone ,+254)!==0) {
      header("Location:form.php?fields=phone");
      exit();
      // check if dob >18
   }elseif($date>18){
      header("Location:form.php?fields=date");
      exit();
   }
   //if all is met
     else{
        header("Location:form.php?fields=success");
        exit();
     }

    }
    

    // echo '<script>
    //         alert("please fill all fields!!!");
    //         location.href="form.phP";
    //         </script>'
        // if(empty($fname =="")){
        //     "<script>
        //             alert('please enter your fast name!!!');
        //             location.href='form.phP';
        //             </script>";
        //     }elseif(empty($lname =="")){
        //         "<script>
        //                 alert('please enter your last name!!!');
        //                 location.href='form.phP';
        //                 </script>";
        //     }elseif(empty($fname =="")){
        //         "<script>
        //                 alert('please enter your fast name!!!');
        //                 location.href='form.phP';
        //                 </script>";
        //     }else{
        //             if (strlen($password) < 15){
        //                 echo "<script>
        //                 alert ('password must have atleast 15 characters!');
        //                 location.href = 'form.php';
        //                 </script>";
        //     }else{
        //         if (strlen($password !== $retypepassword)){
        //             echo "<script>
        //             alert ('password must have atleast 15 characters!');
        //             location.href = 'form.php';
        //             </script>";
        //         }
            























            }
        }
            
    }
