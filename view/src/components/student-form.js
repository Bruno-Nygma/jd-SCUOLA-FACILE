import { createRef } from "just-dom";
import { jd } from "../jd.config";
import { createSignal } from "@just-dom/signals";

export function StudentForm({ student, onSubmit } = {}) {
    console.log(student);
    const btnRef = createRef();

    return jd.form({
        ref: (el) => {
            el.addEventListener('submit', e => {
                e.preventDefault();
                if (onSubmit && typeof onSubmit === 'function') {
                    btnRef.current.disabled = true;
                    btnRef.current.innerHTML = '';
                    btnRef.current.append(jd.lucide('Loader2', { className: 'size-4 animate-spin' }));

                    onSubmit(e).then(() => {
                        console.log('modifica ascoltata da dentro student form');
                    })
                        .finally(() => {
                            btnRef.current.disabled = false;
                            btnRef.current.innerHTML = '';
                            btnRef.current.append(
                                jd.lucide(student ? 'Save' : 'Plus', { className: 'size-4' }),
                                student ? 'Modifica studente' : 'Aggiungi studente'
                            )
                        })
                }
            })
        },
        className: 'space-y-4 mt-6'
    }, [

        //Input Nome
        jd.div({}, [
            jd.label({ className: 'input validator w-full' }, [
                jd.lucide('User2', { className: 'h-[1em] opacity-50' }),
                jd.input({
                    'name': 'name',
                    'type': 'text',
                    'required': true,
                    'placeholder': 'Nome',
                    'minlength': '3',
                    'value': student ? student.name : null
                })
            ]),
            jd.p({ className: 'validator-hint hidden' }, ['Il nome deve avere almeno 3 lettere']),
        ]),

        //Input Cognome
        jd.div({}, [
            jd.label({ className: 'input validator w-full' }, [
                jd.lucide('User2', { className: 'h-[1em] opacity-50' }),
                jd.input({
                    'name': 'surname',
                    'type': 'text',
                    'required': true,
                    'placeholder': 'Cognome',
                    'minlength': '3',
                    'value': student ? student.surname : null
                })
            ]),
            jd.p({ className: 'validator-hint hidden' }, ['Il cognome deve avere almeno 3 lettere'])
        ]),

        //Input Corso
        jd.div({}, [
            jd.label({ className: 'input validator w-full' }, [
                jd.lucide('GraduationCap', { className: 'h-[1em] opacity-50' }),
                jd.input({
                    'name': 'course',
                    'type': 'text',
                    'required': true,
                    'placeholder': 'Corso',
                    'value': student ? student.course : null
                })
            ]),
            jd.p({ className: 'validator-hint hidden' }, ['Il corso è un campo obbligatorio']),
        ]),

        //Input Email
        jd.div({}, [
            jd.label({ className: 'input validator w-full' }, [
                jd.lucide('Mail', { className: 'h-[1em] opacity-50' }),
                jd.input({
                    'name': 'email',
                    'type': 'email',
                    'required': true,
                    'placeholder': 'mail@site.com',
                    'value': student ? student.email : null
                })
            ]),
            jd.p({ className: 'validator-hint hidden' }, ['Inserisci una mail valida'])
        ]),

        //Input Password
        jd.div({}, [
            jd.label({ className: 'input validator w-full' }, [
                jd.lucide('KeyRound', { className: 'h-[1em] opacity-50' }),
                jd.input({
                    'name': 'password',
                    'type': 'password',
                    'required': true,
                    'placeholder': 'Password',
                    'minlength': '8',
                    'pattern': '(?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
                    'title': 'Must be more than 8 characters, including number, lowercase letter, uppercase letter',
                    'autocomplete': 'false',
                    'value': student ? student.password : null
                })
            ]),
            jd.p({ className: 'validator-hint hidden' }, [
                'Deve avere più di 8 caratteri e includere:',
                jd.br(),
                'Almeno un numero',
                jd.br(),
                'Almeno una lettera minuscola',
                jd.br(),
                'Almeno una lettera maiuscola'
            ]),
        ]),

        //Submit
        jd.button({
            ref: btnRef,
            'type': 'submit',
            className: 'btn btn-primary'
        }, [
            jd.lucide(student ? 'Save' : 'Plus', { className: 'size-4' }),
            student ? 'Modifica studente' : 'Aggiungi studente'
        ])
    ])
}



