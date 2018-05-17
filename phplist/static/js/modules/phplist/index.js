import {post} from "../common"

import {formQuestion} from "./templates"

export class ConfirmAccountPHPList {
    constructor(confirmAccount) {
        this.confirmAccount = confirmAccount
    }

    init() {
        this.addToForm()
    }

    addToForm() {
        this.confirmAccount.confirmQuestionsTemplates.push(formQuestion)
        this.confirmAccount.formChecks.push(
            () => document.querySelector('input[name=emaillist]:checked')
        )
        this.confirmAccount.confirmMethods.push(
            () => {
                let emailListRadio = document.querySelector('input[name=emaillist]:checked')
                if (!emailListRadio || emailListRadio.value==='no') {
                    return
                }
                let email = this.confirmAccount.confirmationData.email
                return post(
                    '/proxy/phplist/subscribe_email',
                    {email}
                )
            }
        )
    }


}
