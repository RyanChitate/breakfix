import React from "react";
import { View, Text, TouchableOpacity, StyleSheet } from "react-native";
import { Ionicons } from "@expo/vector-icons";

export default function Question() {
  return (
    <View style={styles.container}>
      {/* Left: Question text */}
      <Text style={styles.text}>HAVE YOU PASSED KFC?</Text>

      {/* Right: Buttons */}
      <View style={styles.buttonsContainer}>
        <TouchableOpacity style={[styles.button, styles.noButton]}>
          <Ionicons name="close" size={24} color="#fff" />
        </TouchableOpacity>
        <TouchableOpacity style={[styles.button, styles.yesButton]}>
          <Ionicons name="checkmark" size={24} color="#fff" />
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: "#222",
    padding: 15,
    borderRadius: 8,
    marginVertical: 10,
    flexDirection: "row",           // <-- Put text & buttons on the same row
    justifyContent: "space-between",// <-- Push them apart
    alignItems: "center",           // <-- Align vertically in the center
  },
  text: {
    color: "#fff",
    fontSize: 18,
    flexShrink: 1,
  },
  buttonsContainer: {
    flexDirection: "row",
  },
  button: {
    width: 45,
    height: 45,
    borderRadius: 8,
    justifyContent: "center",
    alignItems: "center",
    marginLeft: 10,
  },
  noButton: {
    backgroundColor: "#B00000",
  },
  yesButton: {
    backgroundColor: "#00A300",
  },
});
