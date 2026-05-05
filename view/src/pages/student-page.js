import { createRef } from "just-dom";
import { StudentForm } from "../components/student-form";
import { jd } from "../jd.config";

export function StudentPage({ params }) {
    const divRef = createRef();

    fetch(`${import.meta.env.VITE_API_URL}/student/${params.id}`)
        .then(async res => {
            const student = await res.json();
            console.log(student);
            divRef.current.innerHTML = '';
            divRef.current.append(
                jd.div({ className: 'avatar mx-auto' }, [
                    jd.div({ className: 'ring-primary ring-offset-base-100 w-24 rounded-full ring-2 ring-offset-2' }, [
                        jd.img({ src: student.img })
                    ])
                ]),
                jd.p({ className: 'font-bold' }, [`${student.name} ${student.surname}`]),
                jd.p({ className: 'opacity-70' }, [student.email]),
                jd.progress({
                    className: "progress w-56 mx-auto",
                    value: `${student.absence_percentage}`,
                    max: "100"
                })
            )


            divRef.current.append(StudentForm({
                student,
                onSubmit: async (e) => {
                    const formData = new FormData(e.target);
                    const data = Object.fromEntries(formData);
                    data.img = `https://api.dicebear.com/9.x/initials/svg?seed=${data.name}-${data.surname}`
                    return fetch(`${import.meta.env.VITE_API_URL}/student/${student.id}`, {
                        method: 'PATCH',
                        body: JSON.stringify(data),
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    }).then(async res => {
                        const studenteMod = await res.json();
                        // console.log(studenteMod);
                        // p.textContent = `${studenteMod.nome} ${studenteMod.cognome}`;
                        // p1.textContent = `${studenteMod.email}`;
                        // img.setAttribute('src', studenteMod.img);
                    })
                }
            }));
        })
        .catch(err => {
            console.log(err);
        });

    return jd.div({ className: 'flex f-screen justify-center items-center' }, [
        jd.div({ className: 'card bg-base-100 shadow-sm w-96 text-center ' }, [
            jd.div({ ref: divRef, className: 'card-body ' }, [
                jd.lucide('Loader2', { className: 'animate-spin mx-auto' })
            ])
        ])
    ]);
}