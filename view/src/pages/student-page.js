import { createRef } from "just-dom";
import { StudentForm } from "../components/student-form";
import { jd } from "../jd.config";

export function StudentPage({ params }) {
    const divRef = createRef();

    fetch(`http://localhost:5000/api/student/${params.id}`)
        .then(async res => {
            const student = await res.json();
            console.log(student);
            divRef.current.innerHTML = '';
            divRef.current.append(
                jd.div({ className: 'avatar mx-auto' }, [
                    jd.div({ className: 'ring-primary ring-offset-base-100 w-24 rounded-full ring-2 ring-offset-2'}, [
                        jd.img({ src: student.img})
                    ])
                ])
            )
            divRef.current.append(StudentForm(student));
        })
        .catch(err => {
            console.log(err);
        });

    return jd.div({ className: 'flex f-screen justify-center items-center' }, [
        jd.div({ className: 'card bg-base-100 shadow-sm w-96 text-center '}, [
            jd.div({ ref:divRef, className: 'card-body '}, [
                jd.lucide('Loader2', { className: 'animate-spin mx-auto' })
            ])
        ])
    ]);
}