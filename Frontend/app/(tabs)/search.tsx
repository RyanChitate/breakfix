import React from "react";
import { ScrollView, View } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import TopSearchBar from "../../components/ui/TopSearchBar";
import Question from "../../components/ui/Question";
import StoreCard from "../../components/ui/StoreCard";

export default function SearchScreen() {
  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: "#000" }}>
      <TopSearchBar />
      <ScrollView contentContainerStyle={{ padding: 15 }}>
        <Question />
        <StoreCard />
        <StoreCard />
        <StoreCard />
      </ScrollView>
    </SafeAreaView>
  );
}
