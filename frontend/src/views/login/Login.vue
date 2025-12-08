<template>
    <v-main class="white-bg center-content">
        <div class="login-container">
            <div class="login-logo">
             <img src="@/assets\images\manhattan_logo.jpg">
            </div>
            <div class="center-box">
                <h2 class="login-title">เข้าสู่ระบบ</h2>
            </div>
            <form @submit.prevent="handleLogin">
                <div class="form-group">
                    <label for="username">ชื่อผู้ใช้:</label>
                    <input type="text" id="username" v-model="username" :disabled="loading" required />
                </div>

                <div class="form-group">
                    <label for="password">รหัสผ่าน:</label>
                    <input type="password" id="password" v-model="password" :disabled="loading" required />
                </div>
                <button class="login-btn" type="submit" :disabled="loading" > {{ loading ? "กำลังเข้าสู่ระบบ..." : "เข้าสู่ระบบ" }}</button>
            </form>
        </div>
    </v-main>
</template>

<script setup>
import { ref } from "vue";
const loading = ref(false);
const username = ref("");
const password = ref("");

const handleLogin = async () => {
    loading.value = true;
}
</script>

<style scoped>

</style>