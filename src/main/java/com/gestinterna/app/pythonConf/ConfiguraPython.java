package com.gestinterna.app.pythonConf;

import com.gestinterna.app.model.mysql.Pacientes;
import com.gestinterna.app.model.postgresql.Laboratorios;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Engine;
import org.graalvm.polyglot.Source;
import org.graalvm.polyglot.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.io.File;
import java.io.IOException;
import java.util.List;

@Configuration
public class ConfiguraPython {

    @Bean
    public listado_LaboratorioPacientes func_ConfiguraPython(){
        try {
            String venvExePath = new File("/graalenv/bin/graalpy")
                    .getPath()
                    .toString();

            Context context = Context
                    .newBuilder("python")
                    .allowAllAccess(true)
                    .allowNativeAccess(true)
                    .option("python.ForceImportSite", "true")
                    .option("python.PythonPath", ".")
                    .option("python.Executable", venvExePath)
                    .option("python.NativeModules", "true")
                    .build();
            System.out.println("Generación del context correcta...");


            File fichPython = new File("/src/main/python/servicios/python_LaboratorioPacientes.py");
            Source source = Source.newBuilder("python", fichPython).build();

            System.out.println("Generación del Source correcta...");



            context.eval(source);
            System.out.println("Eval realizado correctamente.......");

            /*
            Value recogeFuncionPython = context
                    .getBindings("python")
                    .getMember("HazListaPython");


            String valorDevuelto = recogeFuncionPython
                    .execute()
                    .toString();
            */


            return context
                    .getBindings("python")
                    .getMember("python_LaboratorioPacientes")
                    .as(listado_LaboratorioPacientes.class);

        } catch (IOException ioException) {
            System.out.println("Algo pasó en el Bean de generación del context de python......................");
            System.out.println("-Causa del error: " + ioException.getCause());
            System.out.println("-Mensaje de error: " + ioException.getMessage());
            System.out.println("-Localizado en: " + ioException.getLocalizedMessage());

            return (new listado_LaboratorioPacientes() {
                @Override
                public List<Pacientes> buscaPacientes(Laboratorios laboratorio, Iterable<Pacientes> pacientes) {
                    return null;
                }
            });
        }
    }


}
