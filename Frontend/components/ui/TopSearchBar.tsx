import React from "react";
import { View, TextInput, Text, TouchableOpacity } from "react-native";
import { Ionicons } from "@expo/vector-icons";

export default function TopSearchBar() {
  return (
    <View style={{ backgroundColor: "#B00000", padding: 10 }}>
      {/* Search Bar */}
      <View
        style={{
          flexDirection: "row",
          alignItems: "center",
          backgroundColor: "#fff",
          borderRadius: 8,
          paddingHorizontal: 10,
        }}
      >
        <Ionicons name="search" size={20} color="#666" />
        <TextInput
          placeholder="Search stores..."
          style={{ flex: 1, padding: 8, fontSize: 16 }}
        />
        <TouchableOpacity>
          <Ionicons name="options" size={24} color="#B00000" />
        </TouchableOpacity>
      </View>

      {/* Direction Hint */}
      <Text style={{ marginTop: 8, color: "#fff", fontSize: 16 }}>
        Turn right by the KFC
      </Text>
    </View>
  );
}
