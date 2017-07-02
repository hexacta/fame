import Vue from "vue";
import Match from "@/components/MatchForm";

describe("Match.vue", () => {
  it("should render correct contents", () => {
    const Constructor = Vue.extend(Match);
    const vm = new Constructor().$mount();
    expect(vm.$el.querySelector("div")).to.not.equal(null);
  });
});
