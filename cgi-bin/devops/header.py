#!/usr/bin/python3 


def ip():
    return "34.201.82.13"


def header():
    print('''
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

    <link href="https://fonts.googleapis.com/css?family=Raleway:100,300,400,500,700,900" rel="stylesheet">

    <script src="https://kit.fontawesome.com/2873a80eb4.js" crossorigin="anonymous"></script>


    <!-- Additional CSS Files -->
    <link rel="stylesheet" type="text/css" href="http://'''+ ip() +'''/assets/css/bootstrap.min.css">

    <link rel="stylesheet" type="text/css" href="http://'''+ ip() +'''/assets/css/font-awesome.css">
 
    <link rel="stylesheet" href="http://'''+ ip() +'''/assets/css/templatemo-softy-pinko.css">

</head>

<body>

    <!-- ***** Features Small Start ***** -->
    <section class="section home-feature">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="row">
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- ***** Features Small End ***** -->
    <br/><br/><br/><br/><br/><br/>

    <!-- ***** Testimonials Start ***** -->
    <section class="section" id="testimonials">
        <div class="container">
            <!-- ***** Section Title Start ***** -->
            <div class="row">
                <div class="col-lg-12">
                    <div class="center-heading">
                        <h2 class="section-title">Result</h2>
                    </div>
                </div>
                <div class="offset-lg-3 col-lg-6">
                    <div class="center-text">
                    </div>
                </div>
            </div>
            <!-- ***** Section Title End ***** -->

                            ''')
                

def footer(name):
    print('''<div class="pricing-footer">
                            <h2> &nbsp; &nbsp; </h2>
                            </div>
                            <div class="card-body" align="center">
                                <a href="http://'''+ ip() +'''/'''+ name +'''_menu.html" class="main-button">Back</a>
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                <a href="http://'''+ ip() +'''/" class="main-button">Home</a>
                                <br/><br/>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- ***** Testimonials Item End ***** -->
    </section>
    <!-- ***** Testimonials End ***** -->


    <!-- ***** Footer Start ***** -->
    <footer>
        <div class="container">
            <div class="row">
                <div class="col-lg-12 col-md-12 col-sm-12">
                    <ul class="social">
                        <li><a href="https://www.facebook.com/adarsh994/"><i class="fab fa-facebook"></i></a></li>
                        <li><a href="https://twitter.com/i_adarsh_kr"><i class="fa fa-twitter"></i></a></li>
                        <li><a href="https://www.github.com/i-adarsh"><i class="fab fa-github"></i></a></li>
                        <li><a href="https://www.linkedin.com/in/adarsh-kr/"><i class="fa fa-linkedin"></i></a></li>
                        <li><a href="https://kadarsh994.medium.com/"><i class="fa fa-medium"></i></a></li>
                    </ul>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-12">
                    <p class="copyright">Copyright &copy; 2021 Adarsh Kumar</p>
                </div>
            </div>
        </div>
    </footer>

    <!-- jQuery -->
    <script src="assets/js/jquery-2.1.0.min.js"></script>

    <!-- Bootstrap -->
    <script src="assets/js/popper.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>

    <!-- Plugins -->
    <script src="assets/js/scrollreveal.min.js"></script>
    <script src="assets/js/waypoints.min.js"></script>
    <script src="assets/js/jquery.counterup.min.js"></script>
    <script src="assets/js/imgfix.min.js"></script>

    <!-- Global Init -->
    <script src="assets/js/custom.js"></script>

</body>

</html>
''')
