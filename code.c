#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100

// Employee Structure
struct Employee
{
    int id;
    char name[50];
    float basicSalary;
    float hra;
    float da;
    float grossSalary;
    float tax;
    float netSalary;
};

struct Employee emp[MAX];
int count = 0;

// Function Prototypes
void addEmployee();
void displayEmployees();
void calculateSalary(int index);
void searchEmployee();
void deleteEmployee();
void saveToFile();
void loadFromFile();
void showMenu();

// Add Employee
void addEmployee()
{
    if (count >= MAX)
    {
        printf("Employee limit reached!\n");
        return;
    }

    printf("\nEnter Employee ID: ");
    scanf("%d", &emp[count].id);

    printf("Enter Name: ");
    scanf("%s", emp[count].name);

    printf("Enter Basic Salary: ");
    scanf("%f", &emp[count].basicSalary);

    calculateSalary(count);
    count++;

    printf("Employee Added Successfully!\n");
}

// Calculate Salary
void calculateSalary(int i)
{
    emp[i].hra = emp[i].basicSalary * 0.20;
    emp[i].da = emp[i].basicSalary * 0.10;

    emp[i].grossSalary = emp[i].basicSalary + emp[i].hra + emp[i].da;

    if (emp[i].grossSalary > 50000)
        emp[i].tax = emp[i].grossSalary * 0.10;
    else
        emp[i].tax = emp[i].grossSalary * 0.05;

    emp[i].netSalary = emp[i].grossSalary - emp[i].tax;
}

// Display Employees
void displayEmployees()
{
    if (count == 0)
    {
        printf("No employees found!\n");
        return;
    }

    printf("\n--- Employee Details ---\n");

    for (int i = 0; i < count; i++)
    {
        printf("\nID: %d", emp[i].id);
        printf("\nName: %s", emp[i].name);
        printf("\nBasic Salary: %.2f", emp[i].basicSalary);
        printf("\nHRA: %.2f", emp[i].hra);
        printf("\nDA: %.2f", emp[i].da);
        printf("\nGross Salary: %.2f", emp[i].grossSalary);
        printf("\nTax: %.2f", emp[i].tax);
        printf("\nNet Salary: %.2f\n", emp[i].netSalary);
    }
}

// Search Employee
void searchEmployee()
{
    int id, found = 0;

    printf("Enter Employee ID to search: ");
    scanf("%d", &id);

    for (int i = 0; i < count; i++)
    {
        if (emp[i].id == id)
        {
            printf("\nEmployee Found:\n");
            printf("Name: %s\n", emp[i].name);
            printf("Net Salary: %.2f\n", emp[i].netSalary);
            found = 1;
        }
    }

    if (!found)
        printf("Employee not found!\n");
}

// Delete Employee
void deleteEmployee()
{
    int id, found = 0;

    printf("Enter Employee ID to delete: ");
    scanf("%d", &id);

    for (int i = 0; i < count; i++)
    {
        if (emp[i].id == id)
        {
            for (int j = i; j < count - 1; j++)
            {
                emp[j] = emp[j + 1];
            }
            count--;
            printf("Employee deleted successfully!\n");
            found = 1;
            break;
        }
    }

    if (!found)
        printf("Employee not found!\n");
}

// Save Data to File
void saveToFile()
{
    FILE *fp = fopen("payroll.txt", "w");

    if (fp == NULL)
    {
        printf("File error!\n");
        return;
    }

    for (int i = 0; i < count; i++)
    {
        fprintf(fp, "%d %s %.2f %.2f %.2f %.2f %.2f %.2f\n",
                emp[i].id, emp[i].name,
                emp[i].basicSalary, emp[i].hra,
                emp[i].da, emp[i].grossSalary,
                emp[i].tax, emp[i].netSalary);
    }

    fclose(fp);
    printf("Data saved to file!\n");
}

// Load Data from File
void loadFromFile()
{
    FILE *fp = fopen("payroll.txt", "r");

    if (fp == NULL)
        return;

    count = 0;

    while (fscanf(fp, "%d %s %f %f %f %f %f %f",
                  &emp[count].id,
                  emp[count].name,
                  &emp[count].basicSalary,
                  &emp[count].hra,
                  &emp[count].da,
                  &emp[count].grossSalary,
                  &emp[count].tax,
                  &emp[count].netSalary) != EOF)
    {
        count++;
    }

    fclose(fp);
}

// Menu
void showMenu()
{
    printf("\n=============================\n");
    printf(" EMPLOYEE PAYROLL SYSTEM\n");
    printf("=============================\n");
    printf("1. Add Employee\n");
    printf("2. Display Employees\n");
    printf("3. Search Employee\n");
    printf("4. Delete Employee\n");
    printf("5. Save to File\n");
    printf("6. Exit\n");
    printf("Enter choice: ");
}

// Main Function
int main()
{
    int choice;

    loadFromFile();

    while (1)
    {
        showMenu();
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            addEmployee();
            break;

        case 2:
            displayEmployees();
            break;

        case 3:
            searchEmployee();
            break;

        case 4:
            deleteEmployee();
            break;

        case 5:
            saveToFile();
            break;

        case 6:
            printf("Exiting...\n");
            exit(0);

        default:
            printf("Invalid choice!\n");
        }
    }

    return 0;
}