import Vue from "vue";
import Router from "vue-router";
import HomePage from "@/components/HomePage";
import LeaguePage from "@/components/LeaguePage";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Home",
      component: HomePage
    },
    {
      path: "/:slug",
      name: "League",
      component: LeaguePage,
      props: route => ({
        slug: route.params.slug,
        home: route.query.home,
        away: route.query.away
      })
    }
  ]
});
