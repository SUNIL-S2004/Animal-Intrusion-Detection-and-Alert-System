// import 'package:flutter/material.dart';
// import 'package:flutter_map/flutter_map.dart' as f_map;
// import 'package:latlong2/latlong.dart' as latlng;
// import 'package:flutter_inappwebview/flutter_inappwebview.dart';
//
// void main() {
//   runApp(MyApp());
// }
//
// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       debugShowCheckedModeBanner: false,
//       theme: ThemeData(primarySwatch: Colors.blue),
//       home: HomePage(),
//     );
//   }
// }
//
// class HomePage extends StatelessWidget {
//   final List<Map<String, dynamic>> menuItems = [
//     {'icon': 'assets/icons/img.png', 'title': 'Location', 'page': LocationScreen()},
//     {'icon': 'assets/icons/img_1.png', 'title': 'Live stream Camera', 'page': LiveStreamScreen()},
//     {'icon': 'assets/icons/img_2.png', 'title': 'Notified Alerts', 'page': AlertsScreen()},
//     {'icon': 'assets/icons/img_3.png', 'title': 'Profile', 'page': ProfileScreen()},
//   ];
//
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: Text('AIDAS'),
//         centerTitle: true,
//         backgroundColor: Colors.amber,
//         elevation: 10,
//         shadowColor: Colors.black54,
//       ),
//       body: Container(
//         decoration: BoxDecoration(
//           gradient: LinearGradient(
//             colors: [Colors.yellow.shade200, Colors.orange.shade200],
//             begin: Alignment.topLeft,
//             end: Alignment.bottomRight,
//           ),
//         ),
//         padding: const EdgeInsets.all(16.0),
//         child: GridView.builder(
//           gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
//             crossAxisCount: 2,
//             crossAxisSpacing: 20,
//             mainAxisSpacing: 20,
//           ),
//           itemCount: menuItems.length,
//           itemBuilder: (context, index) {
//             return GestureDetector(
//               onTap: () {
//                 Navigator.push(
//                   context,
//                   MaterialPageRoute(builder: (context) => menuItems[index]['page']),
//                 );
//               },
//               child: Card(
//                 shape: RoundedRectangleBorder(
//                   borderRadius: BorderRadius.circular(15),
//                 ),
//                 elevation: 5,
//                 child: Column(
//                   mainAxisAlignment: MainAxisAlignment.center,
//                   children: [
//                     Container(
//                       width: 60,
//                       height: 60,
//                       decoration: BoxDecoration(
//                         shape: BoxShape.circle,
//                         color: Colors.grey.shade200,
//                       ),
//                       child: Center(
//                         child: Image.asset(menuItems[index]['icon'], width: 40, height: 40),
//                       ),
//                     ),
//                     SizedBox(height: 10),
//                     Text(menuItems[index]['title'], style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
//                   ],
//                 ),
//               ),
//             );
//           },
//         ),
//       ),
//     );
//   }
// }
//
// class LocationScreen extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(title: Text("Animal Detected Location")),
//       body: f_map.FlutterMap(
//         options: f_map.MapOptions(
//           initialCenter: latlng.LatLng(17.4255716, 78.6455365), // Example Coordinates
//           initialZoom: 14.0,
//         ),
//         children: [
//           f_map.TileLayer(
//             urlTemplate: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
//             subdomains: ['a', 'b', 'c'],
//           ),
//           f_map.MarkerLayer(
//             markers: [
//               f_map.Marker(
//                 point: latlng.LatLng(17.4255716, 78.6455365), // Marker Example
//                 width: 40,
//                 height: 40,
//                 child: Icon(Icons.location_pin, color: Colors.red, size: 40),
//               ),
//             ],
//           ),
//         ],
//       ),
//     );
//   }
// }
//
//
// class LiveStreamScreen extends StatefulWidget {
// @override
// _LiveStreamScreenState createState() => _LiveStreamScreenState();
// }
//
// class _LiveStreamScreenState extends State<LiveStreamScreen> {
//   late InAppWebViewController _webViewController;
//   String liveStreamUrl = "http://127.0.0.1:5000/"; // Flask stream URL
//
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(title: Text("Live Stream Camera")),
//       body: InAppWebView(
//           initialUrlRequest: URLRequest(url: WebUri(liveStreamUrl)),
//         onWebViewCreated: (controller) {
//           _webViewController = controller;
//         },
//       ),
//     );
//   }
// }
//
//
// class AlertsScreen extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(title: Text("Notified Alerts")),
//       body: Center(child: Text("Notified Alerts Page")),
//     );
//   }
// }
//
// class ProfileScreen extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(title: Text("Profile")),
//       body: Center(child: Text("Profile Page")),
//     );
//   }
// }


import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart' as f_map;
import 'package:latlong2/latlong.dart' as latlng;
import 'package:flutter_inappwebview/flutter_inappwebview.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.brown,
        scaffoldBackgroundColor: Colors.brown,
      ),
      home: HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  final List<Map<String, dynamic>> menuItems = [
    {'icon': 'assets/icons/img.png', 'title': 'Location', 'page': LocationScreen()},
    {'icon': 'assets/icons/img_1.png', 'title': 'Live stream Camera', 'page': LiveStreamScreen()},
    {'icon': 'assets/icons/img_2.png', 'title': 'Notified Alerts', 'page': AlertsScreen()},
    {'icon': 'assets/icons/img_3.png', 'title': 'Profile', 'page': ProfileScreen()},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('AIDAS', style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: Colors.white)),
        centerTitle: true,
        backgroundColor: Colors.brown,
        elevation: 10,
        shadowColor: Colors.black54,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: GridView.builder(
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 2,
            crossAxisSpacing: 20,
            mainAxisSpacing: 20,
            childAspectRatio: 1,
          ),
          itemCount: menuItems.length,
          itemBuilder: (context, index) {
            return GestureDetector(
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => menuItems[index]['page']),
                );
              },
              child: Card(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(15),
                ),
                elevation: 8,
                color: Colors.brown.shade300,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Container(
                      width: 70,
                      height: 70,
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        color: Colors.white,
                      ),
                      child: Center(
                        child: Image.asset(menuItems[index]['icon'], width: 50, height: 50),
                      ),
                    ),
                    SizedBox(height: 15),
                    Text(
                      menuItems[index]['title'],
                      style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white),
                    ),
                  ],
                ),
              ),
            );
          },
        ),
      ),
    );
  }
}

class LocationScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          "Animal Detected Location",
          style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold,color: Colors.white),
        ),
        centerTitle: true,
        backgroundColor: Colors.brown.shade700,
        elevation: 10,
      ),
      body: f_map.FlutterMap(
        options: f_map.MapOptions(
          initialCenter: latlng.LatLng(13.360552237582999, 80.14265784280022),
          initialZoom: 16.0,
        ),
        children: [
          f_map.TileLayer(
            urlTemplate: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
            subdomains: ['a', 'b', 'c'],
          ),
          f_map.MarkerLayer(
            markers: [
              f_map.Marker(
                point: latlng.LatLng(13.360552237582999, 80.14265784280022),
                width: 50,
                height: 50,
                child: Icon(Icons.location_pin, color: Colors.red, size: 50),
              ),
            ],
          ),
        ],
      ),
    );
  }
}

class LiveStreamScreen extends StatefulWidget {
  @override
  _LiveStreamScreenState createState() => _LiveStreamScreenState();
}

class _LiveStreamScreenState extends State<LiveStreamScreen> {
  late InAppWebViewController _webViewController;
  String liveStreamUrl = "http://127.0.0.1:5000/";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          "Animal Detected Location",
          style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold,color: Colors.white),
        ),
        centerTitle: true,
        backgroundColor: Colors.brown.shade700,
        elevation: 10,
      ),
      body: InAppWebView(
        initialUrlRequest: URLRequest(url: WebUri(liveStreamUrl)),
        onWebViewCreated: (controller) {
          _webViewController = controller;
        },
      ),
    );
  }
}

class AlertsScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Notified Alerts")),
      body: Center(
        child: Text(
          "No alerts available",
          style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.black54),
        ),
      ),
    );
  }
}

class ProfileScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Profile")),
      body: Center(
        child: Text(
          "User Profile",
          style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.black54),
        ),
      ),
    );
  }
}
