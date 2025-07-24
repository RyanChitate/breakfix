import React from "react";
import { View, Text, Image } from "react-native";

export default function WelcomeCard({ username, favouriteMall }: { username: string; favouriteMall: string }) {
  return (
    <View style={{ backgroundColor: "#222", padding: 20, borderRadius: 10 }}>
      <Text style={{ fontSize: 22, fontWeight: "bold", color: "#fff" }}>WELCOME BACK!</Text>
      <Text style={{ fontSize: 18, color: "#fff", marginTop: 5 }}>{username}</Text>
      <Text style={{ fontSize: 14, color: "#aaa", marginTop: 8 }}>
        Your favourite mall: {favouriteMall}
      </Text>
      <Image
        source={require("../../assets/images/image.png")}
        style={{ width: 60, height: 60, borderRadius: 30, marginTop: 10 }}
      />
    </View>
  );
}
