import React from "react";
import { View, Text } from "react-native";

export default function StoreCard() {
  return (
    <View
      style={{
        backgroundColor: "#222",
        padding: 15,
        borderRadius: 8,
        marginVertical: 8,
      }}
    >
      <Text style={{ color: "#fff", fontSize: 18, fontWeight: "bold" }}>
        STORE NAME
      </Text>
      <Text style={{ color: "#aaa" }}>Store Category</Text>
      <Text style={{ color: "#aaa", marginTop: 4 }}>
        Open | 09:00 - 17:00 | Floor Level: 0
      </Text>
      <Text style={{ color: "#ccc", marginTop: 8 }}>
        Placeholder: Recommendations / Promos / Discounts
      </Text>
    </View>
  );
}
