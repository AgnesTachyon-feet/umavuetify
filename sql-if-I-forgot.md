psql -h 127.0.0.1 -U postgres -d umavuetify
\l                      -- list databases
\c dbname               -- เปลี่ยนไปใช้ db อื่น
\q                      -- ออก

\dt                     -- list tables ใน db ปัจจุบัน (schema public)
\dt schema.*            -- list tables ใน schema อื่น เช่น \dt auth.*
\d tablename            -- ดูโครงสร้างตาราง (columns / constraints คร่าว ๆ)
\d+ tablename           -- ดูโครงสร้างตารางแบบละเอียด (มี size / storage)
\dn                     -- list schemas ทั้งหมด
\du                     -- list users / roles ทั้งหมด

\s                      -- ดู history คำสั่งที่เคยพิมพ์ใน psql
\e                      -- เปิด editor (nano/vim) เพื่อแก้ query ล่าสุดแล้วรัน
\r                      -- เคลียร์ query ปัจจุบัน เริ่มพิมพ์ใหม่

\password               -- เปลี่ยนรหัสของ user ปัจจุบัน
\password username      -- เปลี่ยนรหัส user ตามชื่อ เช่น \password umauser

\x                      -- toggle expanded mode (แสดงผลแนวตั้ง อ่านง่ายขึ้น)
\timing                 -- toggle แสดงเวลา query แต่ละคำสั่ง
\pset pager off         -- ปิดการใช้ pager (ไม่ต้องกด space เวลา output ยาว)
\pset border 2          -- ทำเส้นตารางให้ชัดขึ้นนิดนึง