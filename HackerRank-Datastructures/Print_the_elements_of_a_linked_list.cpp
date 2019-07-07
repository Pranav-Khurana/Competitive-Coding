//https://hackerrank-challenge-pdfs.s3.amazonaws.com/1082-print-the-elements-of-a-linked-list-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562480056&Signature=d7PetQ21FWErG4lY0WV3k8MW9UY%3D&response-content-disposition=inline%3B%20filename%3Dprint-the-elements-of-a-linked-list-English.pdf&response-content-type=application%2Fpdf
// Complete the printLinkedList function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;
 * };
 *
 */
void printLinkedList(SinglyLinkedListNode* head) {
    while(head!=NULL)
    {
        cout<<head->data<<"\n";
        head=head->next;

    }
}
