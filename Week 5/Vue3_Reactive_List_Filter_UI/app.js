const { createApp } = Vue;

createApp({

    data() {
        return {
            search: "",
            items: [
                "Laptop",
                "Mobile",
                "Keyboard",
                "Mouse",
                "Monitor",
                "Printer"
            ]
        };
    },

    computed: {
        filteredItems() {
            return this.items.filter(item =>
                item.toLowerCase().includes(this.search.toLowerCase())
            );
        }
    }

}).mount("#app");
