import React from "react";
import { View, Text, StyleSheet, Image } from "react-native";

export default function HeaderBar({ mallName }: { mallName: string }) {
  return (
    <View>
      {/* Top red bar with logo and title */}
      <View style={styles.topBar}>
        <Image
          source={require("../../assets/images/image.png")}
          style={styles.logo}
        />
        <Text style={styles.logoText}>ROAMWISE</Text>
      </View>
      {/* Mall name strip */}
      <View style={styles.mallStrip}>
        <Text style={styles.mallText}>{mallName}</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  topBar: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",      // Center logo + text horizontally
    backgroundColor: "#B00000",
    paddingVertical: 16,           // Slightly taller for visual balance
    paddingHorizontal: 16,
  },
  logo: {
    width: 28,
    height: 28,
    marginRight: 8,
    resizeMode: "contain",
  },
  logoText: {
    color: "#fff",
    fontSize: 20,
    fontWeight: "bold",
  },
  mallStrip: {
    backgroundColor: "#1a1a1a",
    paddingVertical: 10,
    alignItems: "center",          // Center the mall name
    borderBottomColor: "#B00000",  // Thin red underline for style
    borderBottomWidth: 2,
  },
  mallText: {
    color: "#fff",
    fontSize: 16,
  },
});
