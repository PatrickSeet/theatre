/**
 * Created by Badmuthafucker on 10/4/14.
 */
var sorsee = 'ncnhazk4umh5by95u3exrpzk';
var movieOne = 'Dark Knight';
var movieTwo = 'Inception';
var movieThree = 'Toy Story';

$(document).ready(function () {

    $('#info_button1').click(function () {
        $("#showtime").html("");
        var endpoint = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?q=' + movieOne + '&page_limit=10&page=1&apikey=' + sorsee;
        $.ajax({
            url: endpoint,
            type: "GET",
            dataType: "json",
            success: function (data) {
                parseMovie(data);
            }
        })

    });

    $('#info_button2').click(function () {
        $("#showtime").html("");
        var endpoint = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?q=' + movieTwo + '&page_limit=10&page=1&apikey=' + sorsee;
        $.ajax({
            url: endpoint,
            type: "GET",
            dataType: "json",
            success: function (data) {
                parseMovie(data);
            }
        })
    });

    $('#info_button3').click(function () {
        $("#showtime").html("");
        var endpoint = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?q=' + movieThree + '&page_limit=10&page=1&apikey=' + sorsee;
        $.ajax({
            url: endpoint,
            type: "GET",
            dataType: "json",
            success: function (data) {
                parseMovie(data);
            }
        })
    });

});

function parseMovie(data) {

    $('#movie').empty();
    var movieID = data.movies[0].id;
    var endpoint_info = 'http://api.rottentomatoes.com/api/public/v1.0/movies/' + movieID + '.json?apikey=' + sorsee;

    $.ajax({
        url: endpoint_info,
        type: "GET",
        dataType: "json",
        success: function (data) {
            $('#movie_synopsis').html("<p>" + data.synopsis + "</p>")
        }
    });
    $.ajax({
        url: "/get_time/" + 1,
        type: "GET",
        dataType: "json",
        success: function (data) {
            for (var j = 0; j < data.length; j++) {
                $('#showtime').append("<td>" + " " + data[j].time + " " + "</td>");
            }
        }
    });
}

$(document).ready(function(){

    $('#tab1').click(function() {
        var $tbl = $('#showtable');
        var counter = 1;
        for (var i = 1; i < 11; i++) {
            $tbl.append('<tr><td>' + i + 'a' + '</td>' + '<td>' + i + 'b' + '</td><td>' + i + 'c' + '</td></tr>');
        }
    });

});