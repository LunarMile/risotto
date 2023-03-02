
// Initializes our data table which holds all of our csv information, the map image, and the day (default value = 0).
Table data;
PImage map;
int day = 0;

// Import the url of our map image.
String url = "https://api.mapbox.com/styles/v1/emilio-suarez/clcrrzrqf002a15oewtqtzhdu/static/-97.563122,38.068852,3.50/1024x1024?access_token=pk.eyJ1IjoiZW1pbGlvLXN1YXJleiIsImEiOiJjbGNycnc3cXQwYnQyM29wY2xlMGZiamIyIn0.ZKhYT5pyyRoo_wNXMF4Iiw";

// Set the latitude, longitude, and zoom level of our map image.
float cX, cY;
float clon = -97.563122;
float clat = 38.068852;
float zoom = 3.5;


// SETUP
void setup() {
  // Initialize frame size (1024x1024), load the url into our map image as a png.
  size(1024, 1024, P2D);
  map = loadImage(url, "png");

  // Load our csv data into our data table.
  data = loadTable("data/fatalData.csv");

  // Set the center coordinates
  cX = mercX(clon);
  cY = mercY(clat);

  // Set image output
  image(map, 0, 0);
}


// DRAW
void draw() {
  translate(width/2, height/2);
  fill(255);
  textSize(32);
  noStroke();
  String prevDate = "";
  
  
  // Iterate through data backwards to go chronologically.
  for (int i = data.getRowCount()-2; i > 0; i--) {
    
    // Set textbox information
    fill(0);
    rect(10 -width/2, 30 - height/2, 170, 40);
    fill(255);
    
    // Get ith coordinate pair
    TableRow dataRow = data.getRow(i+1);
    float lat = dataRow.getFloat(15);
    float lon = dataRow.getFloat(16);
    float fy = mercY(lat);
    float fx = mercX(lon);
    
    
    

    // If the ith datapoints date is the *same* as its predecesor, then it should only add a point onto the map
    if (dataRow.getString(8).equals(prevDate)) {
      ellipse(fx, fy, 2, 2);

    // If the ith datapoints date is *different* than its predecessor, then it should add a point onto the map, update the text box with the new date, and save the frame as a png
    } else {
      prevDate = dataRow.getString(8);
      day++;
      ellipse(fx, fy, 2, 2);      
      text(prevDate, 20 - width/2, 60 - height/2);
      saveFrame("day" + day + ".png");
      println(prevDate);
    }
  }
  
  // Ensure program does not loop.
  noLoop(); 
}


// Longitude to x  (WEBMercator)
float mercX(float lon) {
  lon = radians(lon);
  float a = (256 / PI) * pow(2, zoom);
  float b = lon + PI;
  return (a * b) - cX;
}


// Lattitude to y  (WEBMercator)
float mercY(float lat) {
  lat = radians(lat);
  float a = (256 / PI) * pow(2, zoom);
  float b = tan(PI / 4 + lat / 2);
  float c = PI - log(b);
  return (a * c) - cY;
}
